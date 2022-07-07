<script setup>
import { ref } from "@vue/reactivity";
import { getUser } from "../services/UserService";
import { runDeployment } from "../services/DeploymentService";
import { logout } from "../services/AuthService";
import Modal from "./Modal.vue";

import { useRouter } from "vue-router";

const router = useRouter();
const user = getUser();
const showPacketTracerModal = ref(false);

const run = async () => {
  showPacketTracerModal.value = true;
  await runDeployment({
    name: user.username,
    label: user.username,
    ip: "192.168.160.1",
  });
  showPacketTracerModal.value = false;
};

const logoutUser = () => {
  logout();
  router.go();
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
    </main>
    <footer>
      <div class="w-icon">
        <i class="fa-brands fa-windows"></i>
      </div>

      <div class="w-user">
        <button class="w-btn">
          <span class="user-username">{{ user.username }}</span>
          <i class="fa-solid fa-user"></i>
        </button>

        <button @click="logoutUser" class="w-btn">
          <span class="user-username">Logout</span>

          <i class="fa-solid fa-right-from-bracket"></i>
        </button>
      </div>
    </footer>

    <Modal
      :isOpen="showPacketTracerModal"
      @closeModal="showPacketTracerModal = false"
    >
      <template #title> Running Packet tracer ... </template>
      <template #content>
        We are running Packet tracer on your computer , please wait for a few
        seconds.
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
  width: 6rem;
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
</style>
