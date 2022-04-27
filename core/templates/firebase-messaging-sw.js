importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

 firebase.initializeApp({
  apiKey: "AIzaSyBjXyJZjKtLoCfnNjAnmFbP9WBLcKrAd8Y",
  authDomain: "crowdsourced-del.firebaseapp.com",
  projectId: "crowdsourced-del",
  storageBucket: "crowdsourced-del.appspot.com",
  messagingSenderId: "282463346408",
  appId: "1:282463346408:web:3d621789de0c4a211d735d",
  measurementId: "G-8KTFD8LNX6"
});

const messaging = firebase.messaging();