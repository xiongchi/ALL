package com.xc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.Map;

/**
 * Created by xiongchi on 2017/11/6.
 */
@Controller
public class MessageController {

    /**
     * 进入信息查询界面
     * @return
     */
    @RequestMapping(value = "/enterMessage")
    public String enterRegister(HttpServletRequest request){
        HttpSession session = request.getSession();
        String userName = (String) session.getAttribute("userName");
        String userIdty = (String) session.getAttribute("userIdty");

        return "/message";
    }





}
