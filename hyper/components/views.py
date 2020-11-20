from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class ComponentsView(LoginRequiredMixin, TemplateView):
    pass

# ecommerce
components_base_ui_accordions_view = ComponentsView.as_view(template_name="components/base-ui/accordions.html")
components_base_ui_alerts_view = ComponentsView.as_view(template_name="components/base-ui/alerts.html")
components_base_ui_avatars_view = ComponentsView.as_view(template_name="components/base-ui/avatars.html")
components_base_ui_badges_view = ComponentsView.as_view(template_name="components/base-ui/badges.html")
components_base_ui_breadcrumb_view = ComponentsView.as_view(template_name="components/base-ui/breadcrumb.html")
components_base_ui_buttons_view = ComponentsView.as_view(template_name="components/base-ui/buttons.html")
components_base_ui_cards_view = ComponentsView.as_view(template_name="components/base-ui/cards.html")
components_base_ui_carousel_view = ComponentsView.as_view(template_name="components/base-ui/carousel.html")
components_base_ui_dropdowns_view = ComponentsView.as_view(template_name="components/base-ui/dropdowns.html")
components_base_ui_embed_video_view = ComponentsView.as_view(template_name="components/base-ui/embed-video.html")
components_base_ui_grid_view = ComponentsView.as_view(template_name="components/base-ui/grid.html")
components_base_ui_list_group_view = ComponentsView.as_view(template_name="components/base-ui/list-group.html")
components_base_ui_media_object_view = ComponentsView.as_view(template_name="components/base-ui/media-object.html")
components_base_ui_modals_view = ComponentsView.as_view(template_name="components/base-ui/modals.html")
components_base_ui_notifications_view = ComponentsView.as_view(template_name="components/base-ui/notifications.html")
components_base_ui_pagination_view = ComponentsView.as_view(template_name="components/base-ui/pagination.html")
components_base_ui_popovers_view = ComponentsView.as_view(template_name="components/base-ui/popovers.html")
components_base_ui_progress_view = ComponentsView.as_view(template_name="components/base-ui/progress.html")
components_base_ui_ribbons_view = ComponentsView.as_view(template_name="components/base-ui/ribbons.html")
components_base_ui_spinners_view = ComponentsView.as_view(template_name="components/base-ui/spinners.html")
components_base_ui_tabs_view = ComponentsView.as_view(template_name="components/base-ui/tabs.html")
components_base_ui_tooltips_view = ComponentsView.as_view(template_name="components/base-ui/tooltips.html")
components_base_ui_typography_view = ComponentsView.as_view(template_name="components/base-ui/typography.html")

# extended
components_extended_dragula_view = ComponentsView.as_view(template_name="components/extended/dragula.html")
components_extended_range_slider_view = ComponentsView.as_view(template_name="components/extended/range-slider.html")
components_extended_ratings_view = ComponentsView.as_view(template_name="components/extended/ratings.html")
components_extended_scrollbar_view = ComponentsView.as_view(template_name="components/extended/scrollbar.html")
components_extended_scrollspy_view = ComponentsView.as_view(template_name="components/extended/scrollspy.html")

# widgets
components_widgets_view = ComponentsView.as_view(template_name="components/widgets.html")

# icons
components_icons_dripicons_view = ComponentsView.as_view(template_name="components/icons/dripicons.html")
components_icons_mdi_view = ComponentsView.as_view(template_name="components/icons/mdi.html")
components_icons_unicons_view = ComponentsView.as_view(template_name="components/icons/unicons.html")

# charts
components_charts_brite_view = ComponentsView.as_view(template_name="components/charts/brite.html")
components_charts_chartjs_view = ComponentsView.as_view(template_name="components/charts/chartjs.html")
components_charts_sparkline_view = ComponentsView.as_view(template_name="components/charts/sparkline.html")

# charts
# -> apex
components_charts_apex_area_view = ComponentsView.as_view(template_name="components/charts/apex/area.html")
components_charts_apex_bar_view = ComponentsView.as_view(template_name="components/charts/apex/bar.html")
components_charts_apex_bubble_view = ComponentsView.as_view(template_name="components/charts/apex/bubble.html")
components_charts_apex_candlestick_view = ComponentsView.as_view(template_name="components/charts/apex/candlestick.html")
components_charts_apex_column_view = ComponentsView.as_view(template_name="components/charts/apex/column.html")
components_charts_apex_heatmap_view = ComponentsView.as_view(template_name="components/charts/apex/heatmap.html")
components_charts_apex_line_view = ComponentsView.as_view(template_name="components/charts/apex/line.html")
components_charts_apex_mixed_view = ComponentsView.as_view(template_name="components/charts/apex/mixed.html")
components_charts_apex_pie_view = ComponentsView.as_view(template_name="components/charts/apex/pie.html")
components_charts_apex_radar_view = ComponentsView.as_view(template_name="components/charts/apex/radar.html")
components_charts_apex_radialbar_view = ComponentsView.as_view(template_name="components/charts/apex/radialbar.html")
components_charts_apex_scatter_view = ComponentsView.as_view(template_name="components/charts/apex/scatter.html")
components_charts_apex_sparklines_view = ComponentsView.as_view(template_name="components/charts/apex/sparklines.html")

# tables
components_tables_basic_view = ComponentsView.as_view(template_name="components/tables/basic.html")
components_tables_datatable_view = ComponentsView.as_view(template_name="components/tables/datatable.html")

# maps
components_maps_google_view = ComponentsView.as_view(template_name="components/maps/google.html")
components_maps_vector_view = ComponentsView.as_view(template_name="components/maps/vector.html")
