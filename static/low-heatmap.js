Plotly.d3.csv("/static/csv/installs_ecost.csv", function (err, rows) {
  function unpack(rows, key) {
    return rows.map(function (row) {
      return row[key];
    });
  }

  var temp = unpack(rows, 'size_one');
  console.log(temp);
  var hold_converted = []

  for (i = 0; i < temp.length; i++) {
    var temp_var = parseFloat(temp[i]);
    console.log(typeof temp_var);
    hold_converted.push(temp_var);


  }

  console.log(hold_converted);

  /* Change colorscale */

  var data = [{
    type: 'choropleth',
    locationmode: 'USA-states',
    locations: unpack(rows, 'abbr'),
    z: hold_converted,
    text: unpack(rows, 'Range'),
    colorscale: [
      [0, '#F87171'],[0.5,'#F8F871'] ,[1, '#71F871']
  ]
  }];

  var layout = {
    title: 'Low Capacity Installations',
    geo: {
      scope: 'usa',
      showlakes: true,
      lakecolor: 'rgb(255,255,255)'
    }
  };

  Plotly.plot(lowDiv, data, layout, {
    showLink: false
  });

});