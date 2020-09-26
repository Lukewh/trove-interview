    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawBoxPlot);

    function drawBoxPlot() {

      var array = [
        ['a', 100, 90, 110, 85, 96, 104, 120],
        ['b', 120, 95, 130, 90, 113, 124, 140],
        ['c', 130, 105, 140, 100, 117, 133, 139],
        ['d', 90, 85, 95, 85, 88, 92, 95],
        ['e', 70, 74, 63, 67, 69, 70, 72],
        ['f', 30, 39, 22, 21, 28, 34, 40],
        ['g', 80, 77, 83, 70, 77, 85, 90],
        ['h', 100, 90, 110, 85, 95, 102, 110]
      ];

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'x');
      data.addColumn('number', 'series0');
      data.addColumn('number', 'series1');
      data.addColumn('number', 'series2');
      data.addColumn('number', 'series3');
      data.addColumn('number', 'series4');
      data.addColumn('number', 'series5');
      data.addColumn('number', 'series6');

      data.addColumn({id:'max', type:'number', role:'interval'});
      data.addColumn({id:'min', type:'number', role:'interval'});
      data.addColumn({id:'firstQuartile', type:'number', role:'interval'});
      data.addColumn({id:'median', type:'number', role:'interval'});
      data.addColumn({id:'thirdQuartile', type:'number', role:'interval'});

      data.addRows(getBoxPlotValues(array));

      /**
       * Takes an array of input data and returns an
       * array of the input data with the box plot
       * interval data appended to each row.
       */
      function getBoxPlotValues(array) {

        for (var i = 0; i < array.length; i++) {

          var arr = array[i].slice(1).sort(function (a, b) {
            return a - b;
          });

          var max = arr[arr.length - 1];
          var min = arr[0];
          var median = getMedian(arr);

          // First Quartile is the median from lowest to overall median.
          var firstQuartile = getMedian(arr.slice(0, 4));

          // Third Quartile is the median from the overall median to the highest.
          var thirdQuartile = getMedian(arr.slice(3));

          array[i][8] = max;
          array[i][9] = min
          array[i][10] = firstQuartile;
          array[i][11] = median;
          array[i][12] = thirdQuartile;
        }
        return array;
      }

      /*
       * Takes an array and returns
       * the median value.
       */
      function getMedian(array) {
        var length = array.length;

        /* If the array is an even length the
         * median is the average of the two
         * middle-most values. Otherwise the
         * median is the middle-most value.
         */
        if (length % 2 === 0) {
          var midUpper = length / 2;
          var midLower = midUpper - 1;

          return (array[midUpper] + array[midLower]) / 2;
        } else {
          return array[Math.floor(length / 2)];
        }
      }

      var options = {
          title:'Box Plot',
          height: 500,
          legend: {position: 'none'},
          hAxis: {
            gridlines: {color: '#fff'}
          },
          lineWidth: 0,
          series: [{'color': '#D3362D'}],
          intervals: {
            barWidth: 1,
            boxWidth: 1,
            lineWidth: 2,
            style: 'boxes'
          },
          interval: {
            max: {
              style: 'bars',
              fillOpacity: 1,
              color: '#777'
            },
            min: {
              style: 'bars',
              fillOpacity: 1,
              color: '#777'
            }
          }
      };

      var chart = new google.visualization.LineChart(document.getElementById('box_plot'));

      chart.draw(data, options);
    }

