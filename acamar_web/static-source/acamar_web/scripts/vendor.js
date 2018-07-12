/* eslint-disable */
var map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: screen.width <= 768 ? {
            lat: 50.09434,
            lng: 14.445151
        } : {lat: 50.093933, lng: 14.442251}, zoom: 17, draggable: !1
    });
    var e = new google.maps.Marker({
        position: {lat: 50.09412, lng: 14.445091},
        map: map,
        icon: "static/images/marker.png"
    });
    new google.maps.InfoWindow({
        content: '<div class="circle-wrapper"><div class="circle-content"><h3 class="title-map text-center">Kanceláře máme<br />v centru Prahy</h3><div><div class="d-flex justify-content-center"><div class="d-flex align-items-start flex-column pl-2"><div class="d-flex align-items-center pb-3"><div><img class="pr-2 pr-md-3" src="static/images/small-icons/location2.png"/></div><div><p class="m-0 text-map"><strong>Karolínská 654/2<br />186 00 Praha</strong></p></div></div><div class="d-flex align-items-center pb-3"><img class="pr-2 pr-md-3" src="static/images/small-icons/write.png"/><div><p class="m-0 text-map">IČ: 777 777 777</p><p class="m-0 text-map">DIČ: 777 777 777</p></div></div><div class="d-flex align-items-center pb-3"><div><img class="pr-2 pr-md-3" src="static/images/small-icons/message.png"/></div><div><p class="m-0 text-map">Telefon: 731 544 584</p><p class="m-0 text-map">E-mail: info@acamar.cz</p></div></div></div></div></div></div></div>',
        maxWidth: "auto",
        pixelOffset: {width: 200, height: 200}
    }).open(map, e)
}

!function (e) {
    (jQuery.browser = jQuery.browser || {}).mobile = /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(e) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(e.substr(0, 4))
}(navigator.userAgent || navigator.vendor || window.opera), $(document).ready(function () {
    $("body").on("click", function () {
        $(".navbar-collapse").removeClass("show"), $(".site-header").removeClass("open-menu"), $(".dropdown-menu").removeClass("show")
    }), $(".site-header").click(function (e) {
        e.stopPropagation()
    }), $(".navbar-toggler").on("click", function () {
        $(".site-header").hasClass("open-menu") ? $(".site-header").removeClass("open-menu") : $(".site-header").addClass("open-menu"), $(".navbar-collapse").hasClass("show") ? $(".navbar-collapse").removeClass("show") : $(".navbar-collapse").addClass("show")
    }), $(".dropdown-toggle").on("click", function () {
        $(".dropdown-menu").hasClass("show") ? $(".dropdown-menu").removeClass("show") : $(".dropdown-menu").addClass("show")
    })
});