package com.example.ms_patient.entities;
import javax.persistence.*;
import java.util.*;

import com.example.ms_patient.models.Ordonnance;
import lombok.*;
import com.fasterxml.jackson.annotation.JsonProperty;
@Entity
 @Data @AllArgsConstructor @NoArgsConstructor
public class Patient{
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String nom;

@Transient
Collection<Ordonnance> ordonnances;

}