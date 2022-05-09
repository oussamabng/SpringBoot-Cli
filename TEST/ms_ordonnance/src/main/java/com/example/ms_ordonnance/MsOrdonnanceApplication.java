package com.example.ms_ordonnance;

import com.example.ms_ordonnance.entities.Ordonnance;
import com.example.ms_ordonnance.repositories.OrdonnanceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

import java.sql.Date;

@SpringBootApplication

public class MsOrdonnanceApplication implements CommandLineRunner {

    @Autowired
    private OrdonnanceRepository ordonnanceRepository;

    public static void main(String[] args) {
        SpringApplication.run(MsOrdonnanceApplication.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        Ordonnance ordonnance = new Ordonnance();
        ordonnance.setDate(Date.valueOf("2020-01-01"));
        ordonnance.setContenu("ordonnance 1");
        ordonnance.setPatientId(1L);

        Ordonnance ordonnance2 = new Ordonnance();
        ordonnance2.setDate(Date.valueOf("2020-01-01"));
        ordonnance2.setContenu("ordonnance 2");
        ordonnance2.setPatientId(1L);


        ordonnanceRepository.save(ordonnance);
        ordonnanceRepository.save(ordonnance2);
    }
}
