from django.urls import path

from .views import (

    components_base_ui_accordions_view,
    components_base_ui_alerts_view,
    components_base_ui_avatars_view,
    components_base_ui_badges_view,
    components_base_ui_breadcrumb_view,
    components_base_ui_buttons_view,
    components_base_ui_cards_view,
    components_base_ui_carousel_view,
    components_base_ui_dropdowns_view,
    components_base_ui_embed_video_view,
    components_base_ui_grid_view,
    components_base_ui_list_group_view,
    components_base_ui_media_object_view,
    components_base_ui_modals_view,
    components_base_ui_notifications_view,
    components_base_ui_pagination_view,
    components_base_ui_popovers_view,
    components_base_ui_progress_view,
    components_base_ui_ribbons_view,
    components_base_ui_spinners_view,
    components_base_ui_tabs_view,
    components_base_ui_tooltips_view,
    components_base_ui_typography_view,

    components_extended_dragula_view,
    components_extended_range_slider_view,
    components_extended_ratings_view,
    components_extended_scrollbar_view,
    components_extended_scrollspy_view,

    components_widgets_view,

    components_icons_dripicons_view,
    components_icons_mdi_view,
    components_icons_unicons_view,

    components_charts_brite_view,
    components_charts_chartjs_view,
    components_charts_sparkline_view,

    components_charts_apex_area_view,
    components_charts_apex_bar_view,
    components_charts_apex_bubble_view,
    components_charts_apex_candlestick_view,
    components_charts_apex_column_view,
    components_charts_apex_heatmap_view,
    components_charts_apex_line_view,
    components_charts_apex_mixed_view,
    components_charts_apex_pie_view,
    components_charts_apex_radar_view,
    components_charts_apex_radialbar_view,
    components_charts_apex_scatter_view,
    components_charts_apex_sparklines_view,

    components_tables_basic_view,
    components_tables_datatable_view,

    components_maps_google_view,
    components_maps_vector_view,
    )


app_name = "components"
urlpatterns = [

    # base_ui
    path("base_ui/accordions", view=components_base_ui_accordions_view, name="components.base_ui.accordions"),
    path("base_ui/alerts", view=components_base_ui_alerts_view, name="components.base_ui.alerts"),
    path("base_ui/avatars", view=components_base_ui_avatars_view, name="components.base_ui.avatars"),
    path("base_ui/badges", view=components_base_ui_badges_view, name="components.base_ui.badges"),
    path("base_ui/breadcrumb", view=components_base_ui_breadcrumb_view, name="components.base_ui.breadcrumb"),
    path("base_ui/buttons", view=components_base_ui_buttons_view, name="components.base_ui.buttons"),
    path("base_ui/cards", view=components_base_ui_cards_view, name="components.base_ui.cards"),
    path("base_ui/carousel", view=components_base_ui_carousel_view, name="components.base_ui.carousel"),
    path("base_ui/dropdowns", view=components_base_ui_dropdowns_view, name="components.base_ui.dropdowns"),
    path("base_ui/embed-video", view=components_base_ui_embed_video_view, name="components.base_ui.embed-video"),
    path("base_ui/grid", view=components_base_ui_grid_view, name="components.base_ui.grid"),
    path("base_ui/list-group", view=components_base_ui_list_group_view, name="components.base_ui.list-group"),
    path("base_ui/media-object", view=components_base_ui_media_object_view, name="components.base_ui.media-object"),
    path("base_ui/modals", view=components_base_ui_modals_view, name="components.base_ui.modals"),
    path("base_ui/notifications", view=components_base_ui_notifications_view, name="components.base_ui.notifications"),
    path("base_ui/pagination", view=components_base_ui_pagination_view, name="components.base_ui.pagination"),
    path("base_ui/popovers", view=components_base_ui_popovers_view, name="components.base_ui.popovers"),
    path("base_ui/progress", view=components_base_ui_progress_view, name="components.base_ui.progress"),
    path("base_ui/ribbons", view=components_base_ui_ribbons_view, name="components.base_ui.ribbons"),
    path("base_ui/spinners", view=components_base_ui_spinners_view, name="components.base_ui.spinners"),
    path("base_ui/tabs", view=components_base_ui_tabs_view, name="components.base_ui.tabs"),
    path("base_ui/tooltips", view=components_base_ui_tooltips_view, name="components.base_ui.tooltips"),
    path("base_ui/typography", view=components_base_ui_typography_view, name="components.base_ui.typography"),
   
    # extended
    path("extended/dragula", view=components_extended_dragula_view, name="components.extended.dragula"),
    path("extended/range-slider", view=components_extended_range_slider_view, name="components.extended.range-slider"),
    path("extended/ratings", view=components_extended_ratings_view, name="components.extended.ratings"),
    path("extended/scrollbar", view=components_extended_scrollbar_view, name="components.extended.scrollbar"),
    path("extended/scrollspy", view=components_extended_scrollspy_view, name="components.extended.scrollspy"),
    
    # widgets
    path("extended/widgets", view=components_widgets_view, name="components.widgets"),

    # icons
    path("icons/dripicons", view=components_icons_dripicons_view, name="components.icons.dripicons"),
    path("icons/mdi", view=components_icons_mdi_view, name="components.icons.mdi"),
    path("icons/unicons", view=components_icons_unicons_view, name="components.icons.unicons"),
    
    # charts
    path("charts/brite", view=components_charts_brite_view, name="components.charts.brite"),
    path("charts/chartjs", view=components_charts_chartjs_view, name="components.charts.chartjs"),
    path("charts/sparkline", view=components_charts_sparkline_view, name="components.charts.sparkline"),
    
    # charts
    # -> apex
    path("charts/apex/area", view=components_charts_apex_area_view, name="components.charts.apex.area"),
    path("charts/apex/bar", view=components_charts_apex_bar_view, name="components.charts.apex.bar"),
    path("charts/apex/bubble", view=components_charts_apex_bubble_view, name="components.charts.apex.bubble"),
    path("charts/apex/candlestick", view=components_charts_apex_candlestick_view, name="components.charts.apex.candlestick"),
    path("charts/apex/column", view=components_charts_apex_column_view, name="components.charts.apex.column"),
    path("charts/apex/heatmap", view=components_charts_apex_heatmap_view, name="components.charts.apex.heatmap"),
    path("charts/apex/line", view=components_charts_apex_line_view, name="components.charts.apex.line"),
    path("charts/apex/mixed", view=components_charts_apex_mixed_view, name="components.charts.apex.mixed"),
    path("charts/apex/pie", view=components_charts_apex_pie_view, name="components.charts.apex.pie"),
    path("charts/apex/radar", view=components_charts_apex_radar_view, name="components.charts.apex.radar"),
    path("charts/apex/radialbar", view=components_charts_apex_radialbar_view, name="components.charts.apex.radialbar"),
    path("charts/apex/scatter", view=components_charts_apex_scatter_view, name="components.charts.apex.scatter"),
    path("charts/apex/sparklines", view=components_charts_apex_sparklines_view, name="components.charts.apex.sparklines"),

    # tables
    path("tables/basic", view=components_tables_basic_view, name="components.tables.basic"),
    path("tables/datatable", view=components_tables_datatable_view, name="components.tables.datatable"),

    # maps
    path("maps/google", view=components_maps_google_view, name="components.maps.google"),
    path("maps/vector", view=components_maps_vector_view, name="components.maps.vector"),

]
