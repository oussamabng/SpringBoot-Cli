package com.example.gateway.defaultResponse;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.Date;
import java.util.ArrayList;
import java.util.List;

@RestController
public class CircuitBreakerController {
    @GetMapping("/defaultOrdonnances")
    public List<Ordonnance> OrdonnanceFallback(){
        List<Ordonnance> ordonnances = new ArrayList<Ordonnance>();
        ordonnances.add(
                new Ordonnance(Date.valueOf("2020-01-01"), "contenue 1")
        );
        return ordonnances;
    }
}