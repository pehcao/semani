/**
 * Created by predix on 9/29/16.
 */



function myFunction() {
    var texto = document.getElementById("fname").value
    if (!texto) {
        console.log("hosfihsdioñh");
    }
    console.log(texto);
    location.replace("http://localhost:9000/second?flight=" + texto)
}
