package com.example.gateway.defaultResponse;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data @AllArgsConstructor @NoArgsConstructor
public class Ordonnance {
    private Date date;
    private String contenu;
}
