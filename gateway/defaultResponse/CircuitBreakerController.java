
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class CircuitBreakerController {

    @GetMapping("/defaultFormations")
    public List<Formation> FormationFallback() {

        List<Formation> formations = new ArrayList<>();
        formations.add(new Formation(1L, "php", 0));
        formations.add(new Formation(2L, "SpringBoot", 0));

        return formations;
    }

}