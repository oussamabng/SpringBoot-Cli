package com.example.name_of_the_project.entities;
import javax.persistence.*;
import java.util.*;
import lombok.*;
import com.fasterxml.jackson.annotation.JsonProperty;
@Entity @Data @AllArgsConstructor @NoArgsConstructor
public class User{
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
@OneToMany(mappedBy = "project",cascade = CascadeType.ALL,fetch = FetchType.LAZY)
Collection<User> users;
}