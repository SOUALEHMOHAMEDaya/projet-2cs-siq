<script setup>
import { reactive, ref } from "@vue/reactivity";
import { getUser } from "../services/UserService";
import { runDeployment } from "../services/DeploymentService";
import { logout } from "../services/AuthService";
import { createUser } from "../services/UserService";
import Modal from "./Modal.vue";

import { useRouter } from "vue-router";

const router = useRouter();
const currentUser = getUser();
const showPacketTracerModal = ref(false);
const showControllModal = ref(false);

const user = reactive({
  username: "",
  password: "",
  email: "",
  role: "client",
});

const successMessage = ref("");

const run = async () => {
  showPacketTracerModal.value = true;
  await runDeployment({
    name: currentUser.username,
    label: currentUser.username,
    ip: "192.168.160.1",
  });
  showPacketTracerModal.value = false;
};

const logoutUser = () => {
  logout();
  router.go();
};

const registre = () => {
  createUser(user, () => {
    successMessage.value = "Student created succefuly !";
    resetForm();
  });
};

const resetForm = () => {
  user.username = "";
  user.password = "";
  user.email = "";
  user.role = "client";
};
</script>

<template>
  <div class="container">
    <main>
      <button @click="run" class="software">
        <img
          class="software-image"
          src="../assets/images/packet-tracer.png"
          alt="packet-tracer"
        />
        <p class="software-title">Packet tracer</p>
      </button>

      <button @click="showControllModal = true" class="software">
        <img
          class="software-image"
          src="../assets/images/control-panel.webp"
          alt="packet-tracer"
        />
        <p class="software-title">Controll panel</p>
      </button>
    </main>
    <footer>
      <div class="w-icon">
        <i class="fa-brands fa-windows"></i>
      </div>

      <div class="w-user">
        <button class="w-btn">
          <span class="user-username">{{ currentUser.username }}</span>
          <i class="fa-solid fa-users"></i>
        </button>

        <button @click="logoutUser" class="w-btn">
          <span class="user-username">Logout</span>

          <i class="fa-solid fa-right-from-bracket"></i>
        </button>
      </div>
    </footer>

    <Modal
      content=""
      :isOpen="showPacketTracerModal"
      @closeModal="showPacketTracerModal = false"
    >
      <template #title> Running Packet tracer ... </template>
      <template #content>
        We are running Packet tracer on your computer , please wait for a few
        seconds.
      </template>
    </Modal>

    <Modal
      :isOpen="showControllModal"
      @closeModal="showControllModal = false"
    >
      <template #title> Create new Student </template>
      <template #content>
        <p class="success" v-show="successMessage">{{ successMessage }}</p>
        <div class="form">
          <form
            @input="successMessage = ''"
            @submit.prevent="registre"
            class="register-form"
          >
            <input v-model="user.email" type="text" placeholder="Email" />
            <input v-model="user.password" type="text" placeholder="Username" />
            <input
              v-model="user.username"
              type="password"
              placeholder="Password"
            />
            <button>create</button>
          </form>
        </div>
      </template>
    </Modal>
  </div>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  background: url("../assets/images/win.png") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.success {
  color: green;
}

footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 40px;
  background-color: rgba(1, 1, 1, 0.8);
  border-color: rgba(1, 1, 1, 0.8);

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.w-icon {
  margin-left: 1rem;
  color: #fff;
  font-size: large;
}

.w-user {
  margin-right: 0.5rem;
  color: #fff;
  font-size: small;
  display: flex;
}

.user-username {
  margin-right: 0.5rem;
}

.w-btn {
  background-color: transparent;
  color: #fff;
  cursor: pointer;

  padding: 0.5rem;
}

.w-btn:hover {
  background-color: rgba(63, 65, 63, 0.3);
  color: #fff;
}

.w-btn:focus {
  background-color: rgba(63, 65, 63, 0.6);
}

.software {
  display: flex;
  width: 7rem;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  padding: 0.5rem;
  margin: 1rem;
  color: #fff;
  background-color: transparent;
  border: none;
}

.software:hover {
  background-color: rgba(63, 65, 63, 0.3);
  color: #fff;
  border-radius: 1rem;
}

.software:focus {
  background-color: rgba(63, 65, 63, 0.6);
  border-radius: 1rem;
}

.software-image {
  width: 3.5rem;
  height: 3.5rem;
}

.software-title {
  font-size: small;
  font-weight: 300;
}

login-page {
  width: 360px;
  padding: 8% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #ffffff;

  margin-top: 4rem;
  text-align: center;
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4caf50;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #ffffff;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,
.form button:active,
.form button:focus {
  background: #43a047;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4caf50;
  text-decoration: none;
}
</style>
