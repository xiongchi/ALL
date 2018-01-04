package com.xc.repository;

import com.xc.properties.Comments;
import com.xc.properties.Users;
import org.springframework.data.domain.Page;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.repository.PagingAndSortingRepository;

/**
 * Created by xiongchi on 2017/11/6.
 */
public interface CommRepository extends JpaRepository<Comments, Integer>,PagingAndSortingRepository<Comments, Integer> {


}
