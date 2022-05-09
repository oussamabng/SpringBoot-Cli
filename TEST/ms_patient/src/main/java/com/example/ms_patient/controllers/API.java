package com.example.ms_patient.controllers;

import com.example.ms_patient.entities.Patient;
import com.example.ms_patient.models.Ordonnance;
import com.example.ms_patient.proxies.OrdonnanceProxy;
import com.example.ms_patient.repositories.PatientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("api")
public class API {

    @Autowired
    private PatientRepository patientRepository;

    @Autowired
    private OrdonnanceProxy ordonnanceProxy;


    @GetMapping("patient/{id}/ordonnance")
    public Patient getPaatientWithOrdonnance(@PathVariable("id") Long id){
        Patient patient = patientRepository.findById(id).get();
        List<Ordonnance> ordonnances =  ordonnanceProxy.getOrdonnanceByPatientId(patient.getId());
        patient.setOrdonnances(ordonnances);
        return patient;
    }
}
