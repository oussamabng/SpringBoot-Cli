package com.example.name_of_the_project.entities;
import javax.persistence.*;
import java.util.*;
import lombok.*;
import com.fasterxml.jackson.annotation.JsonProperty;
import javax.persistence.Embeddable
;import java.io.Serializable;
@Entity @Data @AllArgsConstructor @NoArgsConstructor
public class Adresse implements Serializable{
private String rue;
private Integer numero;
private String ville;
}