package com.xc.controller;

import com.xc.domain.Result;
import com.xc.properties.Comments;
import com.xc.repository.CommRepository;
import com.xc.utils.ResultUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Map;

/**
 * Created by xiongchi on 2017/11/6.
 */
@Controller
public class CommentsController {

    @Autowired
    private CommRepository commRepository;

    @RequestMapping(value = "/enterComments")
    public String enterRegister(){
        return "/comments";
    }

    @ResponseBody
    @RequestMapping(value = "/comments")
    public Result comments(@RequestParam Map<String, String> map){
        //用户评论内容
        String context = map.get("context");
        //用户评论星级
        String grade = map.get("grade");

        Date date = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String now = dateFormat.format(date);
        Comments comm = new Comments();
        comm.setCommTime(now);
        comm.setCommCont(context);
        comm.setGradeNum(Integer.parseInt(grade));
        Comments c = commRepository.save(comm);
        if(c != null){
            return ResultUtil.success(c);
        }
        return ResultUtil.error(0,"系统错误");
    }


//    public Page<Comments> getComments(@PageableDefault(value = 15)Pageable pageable){
//
//    }
}
