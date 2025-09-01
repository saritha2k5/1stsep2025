package Pkg1;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class jahnavi {

	public static void main(String[] args) {
	
	        LocalDateTime dateTime = LocalDateTime.now();
	        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
	        String formattedDateTime = dateTime.format(formatter);
	        System.out.println("Formatted Date and Time: " + formattedDateTime);
	    }


	}


