
import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Continente No. 4: " + Continentes.AMERICA);
        System.out.println("No. de habitantes en el 4to. continente: " + Continentes.AMERICA.getHabitantes());
    }

    private static void indicarDiaSemana(Dias dias) {
        switch (dias) {
            case LUNES:
                System.out.println("Primer día de la semana (Lunes)");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana (Martes)");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana (Miércoles)");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana (Jueves)");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana (Viernes)");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana (Sábado)");
                break;
            case DOMINGO:
                System.out.println("Último día de la semana (Domingo)");
                break;
            default:
                System.out.println("ERROR: Día no válido o nulo");
                break;
        }
    }
}