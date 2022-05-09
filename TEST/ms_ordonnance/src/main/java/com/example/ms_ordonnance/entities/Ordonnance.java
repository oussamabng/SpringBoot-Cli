package com.example.ms_ordonnance.entities;
import javax.persistence.*;
import java.util.*;
import lombok.*;
import com.fasterxml.jackson.annotation.JsonProperty;
@Entity
 @Data @AllArgsConstructor @NoArgsConstructor
public class Ordonnance{
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private Date date;
private String contenu;
}