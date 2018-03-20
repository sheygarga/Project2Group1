Plotly.d3.csv("/static/csv/skin_map_incidence.csv", function (err, rows) {
  function unpack(rows, key) {
    return rows.map(function (row) {
      return row[key];
    });
  }

  var data = [{
    type: 'choropleth',
    locationmode: 'USA-states',
    locations: unpack(rows, 'State'),
    z: unpack(rows, 'Rate'),
    text: unpack(rows, 'Range'),
    autocolorscale: true
  }];

  var layout = {
    title: 'Rate of Skin Cancer according to the CDC',
    geo: {
      scope: 'usa',
      showlakes: true,
      lakecolor: 'rgb(255,255,255)'
    }
  };

  Plotly.plot(myDiv, data, layout, {
    showLink: false
  });

});