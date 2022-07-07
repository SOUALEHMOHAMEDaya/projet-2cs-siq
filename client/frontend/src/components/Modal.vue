<script setup>
import { ref } from "@vue/reactivity";

defineProps({
  isOpen: {
    type: Boolean,
    default: true,
  },
});

</script>

<template>
  <div v-show="isOpen">
    <div class="modal">
      <button @click="$emit('closeModal')" class="close-modal">&times;</button>
      <h1>
        <slot name="title"></slot>
      </h1>
      <p>
        <slot name="content"></slot>
      </p>
    </div>
    <div class="overlay"></div>
  </div>
</template>

<style scoped>
.hidden {
  display: none;
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;

  background-color: white;
  padding: 4rem;
  border-radius: 5px;
  box-shadow: 0 3rem 5rem rgba(0, 0, 0, 0.3);
  z-index: 10;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(3px);
  z-index: 5;
}

.close-modal {
  position: absolute;
  top: 1.2rem;
  right: 2rem;
  font-size: 3rem;
  color: #333;
  cursor: pointer;
  border: none;
  background: none;
}
</style>
