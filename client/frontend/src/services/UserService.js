

import { decodeToken } from "./JwtService";


const API_URL = "http://127.0.0.1:8000/register";

export const getUser = () => {
    const token = window.localStorage.getItem("_token");

    if (token) {
        return decodeToken(token);
    }
    return null;
}

export const createUser = (user, callback) => {
    return fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user),
    }).then(res => {
        return res.json();
    }).then(res => {
        callback(res);
    });
}

export const isAuthenticated = () => {
    return getUser() !== null;
}



export const isAdmin = () => {
    let user = getUser();
    if (user) {
        return user.role === "admin";
    }
    return false;
}

export const isClient = () => {
    let user = getUser();
    if (user) {
        return user.role === "client";
    }
    return false;
}
