package condicionales;

import javax.swing.JOptionPane;


public class condicionales {
    public static void main (string [] args) {
        int numero, dato = 5;

        numero = Integer.parseInt(JOptionPane . showInputDialog ("Digite un numero: "))
        
        if (numero != dato) {
            JOptionPane.showMessageDialog(null, "El número es diferente de 5");
        }
        else {
            JOptionPane}.showMessageDialog(null, "El número es 5");

        }
    }
