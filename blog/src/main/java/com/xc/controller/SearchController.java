package com.xc.controller;

import com.xc.consts.Consts;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;

/**
 * Created by xiongchi on 2017/11/8.
 */
public class SearchController {

    @RequestMapping(value = "/enterSearch")
    public String enterSearch(HttpSession session){

        if(session.getAttribute("userId") == null){
            return "redirect:/blog/login";
        }
        String userName = (String) session.getAttribute("userName");
        String userIdty = (String) session.getAttribute("userIdty");
        Integer userId = (Integer) session.getAttribute("userId");
        if(Consts.MANAGER.equals(userIdty)){
          
        }else if(Consts.USERS.equals(userIdty)){

        }
        return "/search";
    }


}
