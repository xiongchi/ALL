package com.xc.properties;

import javax.persistence.*;

/**
 * Created by xiongchi on 2017/11/6.
 */
@Entity
@Table(name = "comments")
public class Comments {
    //评论主键
    @Id
    @GeneratedValue
    @Column(name = "comm_id")
    private Integer commId;

    //评论内容
    @Column(name = "comm_count")
    private String commCont;

    //评价星级
    @Column(name = "grade_num")
    private Integer gradeNum;

    //评论时间
    @Column(name = "comm_time")
    private String commTime;

    //被评论快递员时间
    @Column(name = "cur_id")
    private String curId;

    //用户
    @Column(name = "user_id")
    private String userId;


    public Integer getCommId() {
        return commId;
    }

    public void setCommId(Integer commId) {
        this.commId = commId;
    }

    public Integer getGradeNum() {
        return gradeNum;
    }

    public void setGradeNum(Integer gradeNum) {
        this.gradeNum = gradeNum;
    }

    public String getCommCont() {
        return commCont;
    }

    public void setCommCont(String commCont) {
        this.commCont = commCont;
    }

    public String getCommTime() {
        return commTime;
    }

    public void setCommTime(String commTime) {
        this.commTime = commTime;
    }

    public String getCurId() {
        return curId;
    }

    public void setCurId(String curId) {
        this.curId = curId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    @Override
    public String toString() {
        return "Comments{" +
                "commId=" + commId +
                ", commCont='" + commCont + '\'' +
                ", gradeNum=" + gradeNum +
                ", commTime='" + commTime + '\'' +
                ", curId='" + curId + '\'' +
                ", userId='" + userId + '\'' +
                '}';
    }
}
