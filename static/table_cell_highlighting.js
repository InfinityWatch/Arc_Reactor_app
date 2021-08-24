/* TODO: jink to replace theme_utils with that from core */
require.config({
  paths: {
    theme_utils: '../app/simple_xml_examples/theme_utils'
  }
});

require([
    'underscore',
    'jquery',
    'splunkjs/mvc',
    'splunkjs/mvc/tableview',
    'theme_utils',
    'splunkjs/mvc/simplexml/ready!'
], function(_, $, mvc, TableView, themeUtils) {

     // Row Coloring Example with custom, client-side range interpretation

    var isDarkTheme = themeUtils.getCurrentTheme && themeUtils.getCurrentTheme() === 'dark';

    var CustomRangeRenderer = TableView.BaseCellRenderer.extend({
        canRender: function(cell) {
            // Enable this custom cell renderer for both the active_hist_searches and the active_realtime_searches field
            return _(['active_hist_searches', 'active_realtime_searches']).contains(cell.field);
        },
        render: function($td, cell) {
            // Add a class to the cell based on the returned value
            var value = parseFloat(cell.value);

            // Apply interpretation for number of historical searches
            if (cell.field === 'active_hist_searches') {
                if (value > 2) {
                    $td.addClass('range-cell').addClass('range-severe');
                }
                else if (value > 1) {
                    $td.addClass('range-cell').addClass('range-elevated');
                }
                else if (value > 0) {
                    $td.addClass('range-cell').addClass('range-low');
                }
            }

            // Apply interpretation for number of realtime searches
            if (cell.field === 'active_realtime_searches') {
                if (value > 1) {
                    $td.addClass('range-cell').addClass('range-severe');
                }
            }

            if (isDarkTheme) {
              $td.addClass('dark');
            }

            // Update the cell content
            $td.text(value.toFixed(2)).addClass('numeric');
        }
    });

    mvc.Components.get('highlight').getVisualization(function(tableView) {
        // Add custom cell renderer, the table will re-render automatically.
        tableView.addCellRenderer(new CustomRangeRenderer());
    });

});
