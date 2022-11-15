package com.adyen.checkout.web;

import com.adyen.checkout.ApplicationProperty;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@Controller
public class CheckoutController {

    private final Logger log = LoggerFactory.getLogger(CheckoutController.class);
	    RestTemplate restTemplate = new RestTemplate();

    @Autowired
    public CheckoutController(ApplicationProperty applicationProperty) {
        this.applicationProperty = applicationProperty;

        if(this.applicationProperty.getClientKey() == null) {
            log.warn("ADYEN_CLIENT_KEY is undefined ");
        }
    }

    @Autowired
    private ApplicationProperty applicationProperty;

    @GetMapping("/")
    public String index(Model model) {
        return "index";
    }


    @GetMapping("/preview")
    public String preview(@RequestParam String type, Model model) {
        model.addAttribute("type", type);
	if (type=="card"){	
        String url1 ="http://localhost:8081/card";
	model.addAttribute("resp", this.restTemplate.getForObject(url1, String.class));
	}
	if (type=="checkout"){

	String url2 ="http://localhost:8082/checkout";
	model.addAttribute("resp", this.restTemplate.getForObject(url2, String.class));
	}	
        return "preview";
    }

    @GetMapping("/checkout")
    public String checkm(Model model) {
        String url ="http://localhost:8082/checkout";
        model.addAttribute("resp", this.restTemplate.getForObject(url, String.class));
	return "checkout"	;
    } 

     @GetMapping("/card")
         public String card(Model model) {
	     String url ="http://localhost:8081/card";
	     model.addAttribute("resp", this.restTemplate.getForObject(url, String.class));
	     return "card" ;
					     }

     /* @GetMapping("/checkout")
       public String checkout(@RequestParam String type, Model model) {
              model.addAttribute("type", type);
              //model.addAttribute("clientKey", this.applicationProperty.getClientKey()); 
	      if (type=="card"){
		String url1 ="http://localhost:8081/card";
		model.addAttribute("resp", this.restTemplate.getForObject(url1, String.class));
				              }
	      if (type=="checkout"){

	          String url2 ="http://localhost:8082/checkout";
		  model.addAttribute("resp", this.restTemplate.getForObject(url2, String.class));
					              }
	       return ""+ type + "" ;
					      } */

    @GetMapping("/result/{type}")
    public String result(@PathVariable String type, Model model) {
        model.addAttribute("type", type);
	String url ="http://localhost:8081/"+type+"";
        model.addAttribute("resp",this.restTemplate.getForObject(url, String.class));
        return "result";
    }

    @GetMapping("/redirect")
    public String redirect(Model model) {
        model.addAttribute("clientKey", this.applicationProperty.getClientKey());
        return "redirect";
    }
}
