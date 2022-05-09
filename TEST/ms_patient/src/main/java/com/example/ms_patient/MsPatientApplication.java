package com.example.ms_patient;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
public class MsPatientApplication {

    public static void main(String[] args) {
        SpringApplication.run(MsPatientApplication.class, args);
    }

}
