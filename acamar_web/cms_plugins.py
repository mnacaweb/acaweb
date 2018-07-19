# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.db.models.aggregates import Count

from acamar_api.models import PositionCategory, PositionPact, Position
from .models import MainBanner, MainBannerCard, WorkElipse, WorkElipseColumn, ReviewPanel, Review, CoursePanel, \
    CreateTeam, CreateTeamCard, TeamGrid, Logo, LogoPanel, TeamMember, ContactGrid, ContactCard, ContactFormModel, \
    ContactFormPurposeOption, Map, PositionSearch, Quote


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


@plugin_pool.register_plugin
class CoursePanelPlugin(CMSPluginBase):
    name = "Course panel"
    model = CoursePanel
    render_template = "plugins/course_panel/course_panel.html"


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
