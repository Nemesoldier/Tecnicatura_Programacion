class Persona{

    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
        return this._idPersona
    }

    get nombre(){
        this._nombre;
    }

    set nombre(nombre){
        this._nombre =  nombre;
    }

    get apellido(){
        return this._apellido
    }

    set apellido(apellido){
        this._apellido
    }

    get edad(){
        this._edad = edad
    }

    set edad(edad){
        this._edad = edad
    }

    toString (){
        return `
        ${this._idPersona} 
        ${this._nombre}
        ${this.apellido} 
        ${this._edad}`;
    }

    
}
