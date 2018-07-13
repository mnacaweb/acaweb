# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

from .models import MainBanner, MainBannerCard, WorkElipse, WorkElipseColumn, ReviewPanel, Review


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
        reviews = Review.objects.order_by("?").filter(show=True)  # TODO
        context["review"] = reviews[0]
        context["review_ids"] = [x.id for x in reviews]
        return context
