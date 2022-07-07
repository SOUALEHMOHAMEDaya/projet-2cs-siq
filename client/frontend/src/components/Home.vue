<script setup>
import Admin from "./Admin.vue";
import Client from "./Client.vue";

import { isAdmin } from "../services/UserService";

const home = isAdmin() ? Admin : Client;
</script>

<template>
  <component :is="home"></component>
</template>
