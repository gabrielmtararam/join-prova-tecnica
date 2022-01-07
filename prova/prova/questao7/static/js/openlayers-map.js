

content = document.getElementById('popup-content');
var center = ol.proj.transform([76.26, 9.93], 'EPSG:4326', 'EPSG:3857'); //initial position of map
    var view = new ol.View({
        center: center,
        zoom: 2
    });

//raster layer on map
   var OSMBaseLayer = new ol.layer.Tile({
        source: new ol.source.OSM()
    });

 straitSource = new ol.source.Vector({ wrapX: true });
    var straitsLayer = new ol.layer.Vector({
        source: straitSource
    });

 map = new ol.Map({
        layers: [OSMBaseLayer, straitsLayer],
        target: 'map',
        view: view,
        controls: []
    });

   // Popup showing the position the user clicked
    var container = document.getElementById('popup');
    var popup = new ol.Overlay({
        element: container,
        autoPan: true,
        autoPanAnimation: {
            duration: 250
        }
    });
    map.addOverlay(popup);



       map.on('click', function (evt) {
           var feature = map.forEachFeatureAtPixel(evt.pixel, function (feat, layer) {
            return feat;
        }
        );

             if (feature && feature.get('type') == 'Point') {
            var coordinate = evt.coordinate;    //default projection is EPSG:3857 you may want to use ol.proj.transform

            content.innerHTML = feature.get('desc');
            open_modal_edit_marker(feature);
             // alert("aaaa"+coordinate+" id"+feature.get('id'));
        }

     });
  /* Add a pointermove handler to the map to render the popup.*/
    map.on('pointermove', function (evt) {
        var feature = map.forEachFeatureAtPixel(evt.pixel, function (feat, layer) {
            return feat;
        }
        );

        if (feature && feature.get('type') == 'Point') {
            var coordinate = evt.coordinate;    //default projection is EPSG:3857 you may want to use ol.proj.transform

            content.innerHTML = feature.get('desc');
            popup.setPosition(coordinate);
        }
        else {
            popup.setPosition(undefined);

        }
    });

// var data=[{"Lon":19.455128,"Lat":41.310575,"name":"nome1","expire_date":"12/08/2022", "id":2222},
//     {"Lon":16.855165,"Lat":45,"name":"nome2","expire_date":"14/08/2022", "id":3333}];

function addPointGeom(data) {

        data.forEach(function(item) { //iterate through array...
            var longitude = item.Lon,
                latitude = item.Lat,
                name = item.name,
                expire_date = item.expire_date,
                id = item.id,
                iconFeature = new ol.Feature({
                    geometry: new ol.geom.Point(ol.proj.transform([longitude, latitude], 'EPSG:4326', 'EPSG:3857')),
                     id: id,
                     latitude: latitude,
                     longitude: longitude,
                     name: name,
                    expire_date: expire_date,
                     type: 'Point',
                    desc: '<pre> <b>Marcador</b> ' + '<br>' +
                        '' + 'Latitude : ' + latitude + '<br>' +
                        'Longitude: ' + longitude +
                         '<br>' + 'name : ' + name +
                         '<br>' + 'expire_date : ' + expire_date  +
                         '<br>' + 'id : ' + id+
                        '</pre>'
                }),
                iconStyle = new ol.style.Style({
                    image: new ol.style.Circle({
                        radius: 5,
                        stroke: new ol.style.Stroke({
                            color: 'blue'
                        }),
                        fill: new ol.style.Fill({
                            color: [57, 228, 193, 0.84]
                        }),
                    })
                });

            iconFeature.setStyle(iconStyle);

            straitSource.addFeature(iconFeature);
        });
    }// End of function showStraits()

// addPointGeom(data);

