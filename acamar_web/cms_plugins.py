# -*- coding: utf-8 -*-


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.translation import get_language

from acamar_api.models import PositionCategory, PositionPact, Position
from .models import (
    MainBanner,
    MainBannerCard,
    WorkElipse,
    WorkElipseColumn,
    ReviewPanel,
    Review,
    CoursePanel,
    CreateTeam,
    CreateTeamCard,
    TeamGrid,
    Logo,
    LogoPanel,
    ContactGrid,
    ContactCard,
    ContactFormModel,
    ContactFormPurposeOption,
    Map,
    PositionSearch,
    Quote,
    BubblePanel,
    BubbleCard,
    Timeline,
    TimelineItem,
    AcaFriendPanel,
    AcaFriendCard,
    ContactUs,
    GraphSection,
    GraphCard,
    GraphCardText,
    PartnersModel,
    ContactPerson,
    CoursePanelItem,
    CourseLector,
    AcardBenefits,
    AcardBenefitsItem,
    CourseBonusPanel,
    CourseBonusCard,
    CourseProgram,
    CourseProgramItem,
    CourseTermList,
    CourseTermListAdditional,
    CourseGenericRegistration,
    CourseBasicInfo,
    CourseBasicInfoCard,
    PartnersItem,
    CourseEnrollFormModel,
    LoginPluginModel,
    ThanksBanner,
    HtmlText,
    BlockLinks
)


@plugin_pool.register_plugin
class MainBannerPlugin(CMSPluginBase):
    name = "Main Banner"
    model = MainBanner
    child_classes = ["MainBannerCardPlugin"]
    allow_children = True
    exclude = ["background_image"]

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
        (None, {"fields": ("title", "subtitle", "button")}),
        (
            "Person",
            {
                "fields": ("person_name", "person_title", "person_phone", "person_email", "image"),
                "classes": ["wide"],
            },
        ),
        ("Additional link", {"fields": ("more",), "classes": ["collapse"]}),
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
        context = super(PositionSearchPlugin, self).render(
            context, instance, placeholder
        )
        language = get_language()
        positions = Position.objects.filter(lang=language).exclude(slug="")

        context["categories"] = PositionCategory.objects.filter(
            positions__in=positions
        ).annotate(num_positions=Count("positions"))
        context["pacts"] = PositionPact.objects.all()
        context["positions"] = positions
        context["limit"] = instance.limit
        context["more"] = (
            (positions.count() > instance.limit) if instance.limit else False
        )
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
    allow_children = True
    child_classes = ["TimelineItemPlugin"]

    def get_render_template(self, context, instance, placeholder):
        if placeholder.slot == "enroll_in_course":
            return "plugins/timeline/timeline_enroll.html"
        return "plugins/timeline/timeline.html"


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
    render_template = "plugins/partners/partners.html"
    allow_children = True
    child_classes = ["PartnersItemPlugin"]


@plugin_pool.register_plugin
class PartnersItemPlugin(CMSPluginBase):
    name = "Partners - item"
    model = PartnersItem
    render_template = "plugins/partners/partners_item.html"
    require_parent = True
    parent_classes = ["PartnersPlugin"]


@plugin_pool.register_plugin
class CourseLectorPlugin(CMSPluginBase):
    name = "Course lector"
    model = CourseLector
    render_template = "plugins/course/course_lector.html"

    fieldsets = [
        (None, {"fields": ("title", "text")}),
        ("Person", {"fields": ("person_name", "person_title", "person_image")}),
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


@plugin_pool.register_plugin
class CourseBonusPanelPlugin(CMSPluginBase):
    name = "Course Bonus panel"
    model = CourseBonusPanel
    render_template = "plugins/course/course_bonus_panel.html"
    allow_children = True
    child_classes = ["CourseBonusCardPlugin"]


@plugin_pool.register_plugin
class CourseBonusCardPlugin(CMSPluginBase):
    name = "Course Bonus - card"
    model = CourseBonusCard
    render_template = "plugins/course/course_bonus_card.html"
    require_parent = True
    parent_classes = ["CourseBonusPanelPlugin"]


class CourseProgramItemInline(admin.TabularInline):
    model = CourseProgramItem
    min_num = 1


@plugin_pool.register_plugin
class CourseProgramPlugin(CMSPluginBase):
    name = "Course program"
    model = CourseProgram
    render_template = "plugins/course/course_program.html"
    inlines = [CourseProgramItemInline]


class CourseTermListAdditionalInline(admin.TabularInline):
    model = CourseTermListAdditional
    extra = 0


@plugin_pool.register_plugin
class CourseTermListPlugin(CMSPluginBase):
    name = "Course Term list"
    model = CourseTermList
    render_template = "plugins/course/course_term_list.html"
    fieldsets = [
        (None, {"fields": ("title", "subtitle", "button")}),
        (
            "Additional registration",
            {
                "fields": ("additional_registration", "additional_title"),
                "classes": ["collapse"],
            },
        ),
    ]
    inlines = [CourseTermListAdditionalInline]


@plugin_pool.register_plugin
class CourseGenericRegistrationPlugin(CMSPluginBase):
    name = "Course generic registration"
    model = CourseGenericRegistration
    render_template = "plugins/course/course_generic_registration.html"


@plugin_pool.register_plugin
class CourseBasicInfoPlugin(CMSPluginBase):
    name = "Course basic info"
    model = CourseBasicInfo
    render_template = "plugins/course/course_basic_info.html"
    allow_children = True
    child_classes = ["CourseBasicInfoCardPlugin"]


@plugin_pool.register_plugin
class CourseBasicInfoCardPlugin(CMSPluginBase):
    name = "Course basic info - card"
    model = CourseBasicInfoCard
    render_template = "plugins/course/course_basic_info_card.html"
    require_parent = True
    parent_classes = ["CourseBasicInfoPlugin"]


@plugin_pool.register_plugin
class CourseEnrollFormPlugin(CMSPluginBase):
    name = "Course enroll form"
    model = CourseEnrollFormModel
    render_template = "plugins/course/course_enroll_form.html"
    fieldsets = [
        (None, {"fields": ("title", ("submit_text", "thanks_page"))}),
        (
            "Form labels",
            {
                "fields": (
                    ("name_label", "phone_label"),
                    ("email_label", "course_label"),
                    ("expectations_label", "cv_label"),
                    ("cv_picker_label", "selected_text"),
                )
            },
        ),
    ]


@plugin_pool.register_plugin
class LoginPlugin(CMSPluginBase):
    name = "Login form"
    model = LoginPluginModel
    render_template = "plugins/login/login.html"
    fieldsets = [
        (None, {"fields": ("title", "subtitle")}),
        (
            "Form labels",
            {"fields": (("username_label", "password_label"), "button_text")},
        ),
    ]
    cache = False


@plugin_pool.register_plugin
class ThanksBannerPlugin(CMSPluginBase):
    name = "Thank you banner"
    model = ThanksBanner
    render_template = "plugins/thank_you/thanks_banner.html"

@plugin_pool.register_plugin
class HtmlTextPlugin(CMSPluginBase):
    name = "Html text"
    model = HtmlText
    render_template = "plugins/htmltext.html"

@plugin_pool.register_plugin
class BlockLinksPlugin(CMSPluginBase):
    name = "Block with links"
    model = BlockLinks
    render_template = "plugins/blocklinks.html"
