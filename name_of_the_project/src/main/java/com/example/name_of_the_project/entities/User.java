package com.example.name_of_the_project.entities;
import javax.persistence.*;
import java.util.Date;
public class User{
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
private Date date_of_birth;
}