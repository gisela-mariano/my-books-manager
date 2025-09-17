<template>
  <RouterView />
</template>

<script setup lang="ts">
import "@common/design-tokens/static/typography.css";
import { useTheme } from "@global/composables";
import "primeicons/primeicons.css";
import { onMounted } from "vue";
import { RouterView } from "vue-router";

const { setTheme } = useTheme();

onMounted(() => {
  setTheme();
});
</script>

<style lang="scss"></style>
