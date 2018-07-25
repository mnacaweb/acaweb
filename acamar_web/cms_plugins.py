# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.db.models.aggregates import Count

from acamar_api.models import PositionCategory, PositionPact, Position
from .models import MainBanner, MainBannerCard, WorkElipse, WorkElipseColumn, ReviewPanel, Review, CoursePanel, \
    CreateTeam, CreateTeamCard, TeamGrid, Logo, LogoPanel, ContactGrid, ContactCard, ContactFormModel, \
    ContactFormPurposeOption, Map, PositionSearch, Quote, BubblePanel, BubbleCard, Timeline, TimelineItem, \
    AcaFriendPanel, AcaFriendCard, ContactUs, GraphSection, GraphCard, GraphCardText, PartnersModel, ContactPerson, \
    CoursePanelItem, CourseLector, AcardBenefits, AcardBenefitsItem, Link


@plugin_pool.register_plugin
class MainBannerPlugin(CMSPluginBase):
    name = "Main Banner"
    model = MainBanner
    child_classes = ["MainBannerCardPlugin"]
    allow_children = True

    @classmethod
    def get_child_classes(cls, slot, page, instance=None):
        if instance and instance.template != MainBanner.DEFAULT:
            return []
        return super(MainBannerPlugin, cls).get_child_classes(slot, page, instance)

    def get_render_template(self, context, instance, placeholder):
        return "plugins/main_banner/{}.html".format(instance.template)


@plugin_pool.register_plugin
class MainBannerCardPlugin(CMSPluginBase):
    name = "Main banner - card"
    model = MainBannerCard
    require_parent = True
    parent_classes = ["MainBannerPlugin"]
    render_template = "plugins/main_banner/_card.html"


class WorkElipseColumnInline(admin.StackedInline):
    model = WorkElipseColumn
    can_delete = False
    min_num = 3
    max_num = 3


@plugin_pool.register_plugin
class WorkElipsePlugin(CMSPluginBase):
    name = "Work - elipse"
    model = WorkElipse
    render_template = "plugins/work_elipse.html"
    inlines = [WorkElipseColumnInline]

    def get_queryset(self, request):
        qs = super(WorkElipsePlugin, self).get_queryset(request)
        return qs.prefetch_related("columns")


@plugin_pool.register_plugin
class ReviewPanelPlugin(CMSPluginBase):
    name = "Review panel"
    model = ReviewPanel
    render_template = "plugins/review_panel/base.html"

    def render(self, context, instance, placeholder):
        context = super(ReviewPanelPlugin, self).render(context, instance, placeholder)
        reviews = Review.objects.filter(show=True)  # TODO
        context["review"] = reviews.first()
        context["review_ids"] = [x.id for x in reviews]
        return context


@plugin_pool.register_plugin
class LogoPanelPlugin(CMSPluginBase):
    name = "Logo panel"
    model = LogoPanel
    render_template = "plugins/logo_panel/logo_panel.html"
    allow_children = True
    child_classes = ["LogoPlugin"]


@plugin_pool.register_plugin
class LogoPlugin(CMSPluginBase):
    name = "Logo"
    model = Logo
    render_template = "plugins/logo_panel/logo.html"
    require_parent = True
    parent_classes = ["LogoPanelPlugin"]


class CoursePanelItemInline(admin.TabularInline):
    model = CoursePanelItem
    extra = 0


@plugin_pool.register_plugin
class CoursePanelPlugin(CMSPluginBase):
    name = "Course panel"
    model = CoursePanel
    inlines = [CoursePanelItemInline]

    def get_render_template(self, context, instance, placeholder):
        return "plugins/course_panel/course_panel{}.html".format(instance.template)


@plugin_pool.register_plugin
class CreateTeamPlugin(CMSPluginBase):
    name = "Create team - panel"
    model = CreateTeam
    render_template = "plugins/create_team/create_team.html"
    allow_children = True
    child_classes = ["CreateTeamCardPlugin"]


@plugin_pool.register_plugin
class CreateTeamCardPlugin(CMSPluginBase):
    name = "Create team - card"
    model = CreateTeamCard
    render_template = "plugins/create_team/create_team_card.html"
    require_parent = True
    parent_classes = ["CreateTeamPlugin"]


@plugin_pool.register_plugin
class TeamGridPlugin(CMSPluginBase):
    name = "Team grid"
    model = TeamGrid
    render_template = "plugins/team_grid/team_grid.html"


@plugin_pool.register_plugin
class ContactGridPlugin(CMSPluginBase):
    name = "Contact grid"
    model = ContactGrid
    render_template = "plugins/contact/contact_grid.html"
    allow_children = True
    child_classes = ["ContactCardPlugin"]


@plugin_pool.register_plugin
class ContactCardPlugin(CMSPluginBase):
    name = "Contact card"
    model = ContactCard
    render_template = "plugins/contact/contact_card.html"
    require_parent = True
    parent_classes = ["ContactGridPlugin"]


class ContactFormPurposeOptionInline(admin.TabularInline):
    model = ContactFormPurposeOption
    min_num = 1
    extra = 1


@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    name = "Contact form"
    model = ContactFormModel
    render_template = "plugins/contact/contact_form.html"
    inlines = [ContactFormPurposeOptionInline]


@plugin_pool.register_plugin
class ContactUsPlugin(CMSPluginBase):
    name = "Contact us"
    model = ContactUs
    render_template = "plugins/contact/contact_us.html"


@plugin_pool.register_plugin
class ContactPersonPlugin(CMSPluginBase):
    name = "Contact person"
    model = ContactPerson
    render_template = "plugins/contact/contact_person.html"

    fieldsets = [
        (None, {"fields": ("title", "subtitle", "button_text", ("button_link_external", "button_link_internal"))}),
        ("Person", {"fields": ("person_name", "person_title", "person_phone", "image"), "classes": ["wide"]}),
        ("Additional link",
         {"fields": ("more_text", ("more_link_external", "more_link_internal")), "classes": ["collapse"]})
    ]


@plugin_pool.register_plugin
class MapPlugin(CMSPluginBase):
    name = "Map"
    model = Map
    render_template = "plugins/map/map.html"


@plugin_pool.register_plugin
class PositionSearchPlugin(CMSPluginBase):
    name = "Position search"
    model = PositionSearch
    render_template = "plugins/position_search/position_search.html"

    def render(self, context, instance, placeholder):
        context = super(PositionSearchPlugin, self).render(context, instance, placeholder)
        positions = Position.objects.all()

        context["categories"] = PositionCategory.objects.annotate(num_positions=Count("positions"))
        context["pacts"] = PositionPact.objects.all()
        context["positions"] = positions
        context["limit"] = instance.limit
        context["more"] = (positions.count() > instance.limit) if instance.limit else False
        return context


@plugin_pool.register_plugin
class QuotePlugin(CMSPluginBase):
    name = "Quote"
    model = Quote
    render_template = "plugins/quote.html"


@plugin_pool.register_plugin
class BubblePanelPlugin(CMSPluginBase):
    name = "Bubble panel"
    model = BubblePanel
    render_template = "plugins/bubble_panel/bubble_panel.html"
    allow_children = True
    child_classes = ["BubbleCardPlugin"]


@plugin_pool.register_plugin
class BubbleCardPlugin(CMSPluginBase):
    name = "Bubble card"
    model = BubbleCard
    render_template = "plugins/bubble_panel/bubble_card.html"
    require_parent = True
    parent_classes = ["BubblePanelPlugin"]


@plugin_pool.register_plugin
class TimelinePlugin(CMSPluginBase):
    name = "Timeline"
    model = Timeline
    render_template = "plugins/timeline/timeline.html"
    allow_children = True
    child_classes = ["TimelineItemPlugin"]


@plugin_pool.register_plugin
class TimelineItemPlugin(CMSPluginBase):
    name = "Timeline item"
    model = TimelineItem
    render_template = "plugins/timeline/timeline_item.html"
    require_parent = True
    parent_classes = ["TimelinePlugin"]


@plugin_pool.register_plugin
class AcaFriendPanelPlugin(CMSPluginBase):
    name = "AcaFriend panel"
    model = AcaFriendPanel
    render_template = "plugins/acafriend_panel/acafriend_panel.html"
    allow_children = True
    child_classes = ["AcaFriendCardPlugin"]


@plugin_pool.register_plugin
class AcaFriendCardPlugin(CMSPluginBase):
    name = "AcaFriend card"
    model = AcaFriendCard
    render_template = "plugins/acafriend_panel/acafriend_card.html"
    require_parent = True
    parent_classes = ["AcaFriendPanelPlugin"]


@plugin_pool.register_plugin
class GraphSectionPlugin(CMSPluginBase):
    name = "Graph section"
    model = GraphSection
    render_template = "plugins/graph_section/graph_section.html"
    allow_children = True
    child_classes = ["GraphCardPlugin"]

    fieldsets = [(None, {"fields": ("button_text", ("button_link_external", "button_link_internal"))})]


class GraphCardTextInline(admin.TabularInline):
    model = GraphCardText
    max_num = 3
    min_num = 1


@plugin_pool.register_plugin
class GraphCardPlugin(CMSPluginBase):
    name = "Graph card"
    model = GraphCard
    render_template = "plugins/graph_section/graph_card.html"
    require_parent = True
    parent_classes = ["GraphSectionPlugin"]
    inlines = [GraphCardTextInline]


@plugin_pool.register_plugin
class PartnersPlugin(CMSPluginBase):
    name = "Partners"
    model = PartnersModel
    render_template = "plugins/partners.html"


@plugin_pool.register_plugin
class CourseLectorPlugin(CMSPluginBase):
    name = "Course lector"
    model = CourseLector
    render_template = "plugins/course_lector.html"

    fieldsets = [
        (None, {"fields": ("title", "text")}),
        ("Person", {"fields": ("person_name", "person_title", "person_image")})
    ]


@plugin_pool.register_plugin
class AcardBenefitsPlugin(CMSPluginBase):
    name = "A-card benefits"
    model = AcardBenefits
    render_template = "plugins/acard_benefits/acard_benefits.html"
    allow_children = True
    child_classes = ["AcardBenefitsItemPlugin"]


@plugin_pool.register_plugin
class AcardBenefitsItemPlugin(CMSPluginBase):
    name = "A-card benefits - item"
    model = AcardBenefitsItem
    render_template = "plugins/acard_benefits/acard_benefits_item.html"
    require_parent = True
    parent_classes = ["AcardBenefitsPlugin"]
