let months = ["Enero","Febrero","Marzo","Abril","mayo",
    "Junio","julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
];
function getMonth(n){
    if (n < 1 || n > 12){
        throw new Error("Out of range")
    }
    return months[n-1];
}
customElements.log (getMonth(5));