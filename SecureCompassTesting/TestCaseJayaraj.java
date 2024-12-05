<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.servlet.http.HttpServletRequest;

public class SQLInjectionVulnerability {
public void doPost(HttpServletRequest request) {
String username = request.getParameter("username");
String password = request.getParameter("password");

    try {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

        // Prepared statement to prevent SQL injection
        String query = "SELECT * FROM users WHERE username = ? AND password = ?";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, username);
        stmt.setString(2, password);

        ResultSet rs = stmt.executeQuery();
        while (rs.next()) {
            // Process result
        }

        rs.close();
        stmt.close();
        conn.close();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
}
