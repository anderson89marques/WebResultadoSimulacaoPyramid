$(document).ready(function(){
    var cont = 0
    var map = new GMaps({
        div:'#mapa',
        zoom: 16,
        lat: -1.45502,
        lng: -48.5024,
        click: function(e){
            cont += 1;
            map.addMarker({
                lat: e.latLng.lat(),
                lng: e.latLng.lng()
            });
            if(cont > 2){
                map.removeMarkers()
                map.removeRoutes()
                map.removePolylines()
                cont = 0;
            }
        }
    });

    $('#botao').click(function(event){
        event.preventDefault();
        if(cont == 1 ){
            alert("Só tem " + cont + " marcador")
        }else if(cont == 0 ){
            alert("Não tem nenhum marcador")
        }else{
            map.travelRoute({
                origin: [map.markers[0].getPosition().lat(), map.markers[0].getPosition().lng()],
                destination: [map.markers[map.markers.length-1].getPosition().lat(), map.markers[map.markers.length-1].getPosition().lng()],
                travelMode: 'drinving',
                step: function(e){
                    map.drawPolyline({
                        path: e.path,
                        strokeColor: '#131540',
                        strokeOpacity: 0.6,
                        strokeWeight: 6
                    });
                }
            });
            /*map.getRoutes({
                origin: [map.markers[0].getPosition().lat(), map.markers[0].getPosition().lng()],
                destination:[map.markers[map.markers.length-1].getPosition().lat(), map.markers[map.markers.length-1].getPosition().lng()],
                callback: function(e) {
                    new GMaps.Route({
                        map: map,
                        route: e[0],
                        strokeColor: '#336699',
                        strokeOpacity: 0.5,
                        strokeWeight: 10
                    }).forward();
                }
            });*/
        }
    });
});