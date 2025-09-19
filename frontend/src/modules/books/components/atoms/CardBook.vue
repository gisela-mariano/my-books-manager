<template>
  <div class="card-book" :class="`layout-${layout}`">
    <section class="card-book__image-section">
      <div
        class="card-book__image-section__image"
        v-if="book.imageUrl"
        :style="{ backgroundImage: `url(${book.imageUrl})` }"
      />

      <div v-else class="card-book__image-section__container-no-image">
        <i class="pi pi-image" />
        <span>{{ t(`${I18nKeys.BOOKS}.components.cardBook.noImage.message`) }}</span>
      </div>
    </section>

    <footer class="card-book__footer text-ellipsis">
      <h1
        class="text-ellipsis"
        v-tooltip.top="{
          value: book.title,
          class: 'default-tooltip',
        }"
      >
        {{ book.title }}
      </h1>

      <span
        class="text-ellipsis"
        v-tooltip.top="{
          value: authors,
          class: 'default-tooltip',
        }"
      >
        {{ authors }}
      </span>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { I18nKeys } from "@/common/types";
import { DataViewLayout } from "@global/types";
import { BookCardProps } from "@modules/books/types";
import { computed, PropType } from "vue";
import { useI18n } from "vue-i18n";

const props = defineProps({
  book: {
    type: Object as PropType<BookCardProps>,
    required: true,
  },
  layout: {
    type: String as PropType<DataViewLayout>,
    default: DataViewLayout.GRID,
  },
});

const { t } = useI18n();

const authors = computed(() => {
  return props.book.authors
    ? props.book.authors.join(", ")
    : t(`${I18nKeys.BOOKS}.components.cardBook.noAuthor.message`);
});
</script>

<style scoped lang="scss">
$card-border-radius: 10;

.card-book {
  padding: prem(16);
  box-sizing: border-box;
  cursor: pointer;

  display: flex;
  gap: prem(12);

  @include box-shadow(0, 8, 28, -12, #00000029);
  @include border-radius($card-border-radius);

  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;

  &:hover {
    transform: scale(1.05);
    @include box-shadow(0, 12, 28, -12, #00000060);
  }

  &__image-section {
    display: flex;
    justify-content: center;
    align-items: center;

    &__image,
    &__container-no-image {
      width: 148px;
      height: 230px;

      @include border-radius($card-border-radius);
    }

    &__image {
      background-size: cover;
      background-position: center;
    }

    &__container-no-image {
      color: var(--p-slate-200);
      background-color: var(--p-slate-600);
      gap: prem(8);

      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

      i {
        font-size: 1.2rem;
      }

      span {
        text-align: center;
      }
    }
  }

  .card-book__footer {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-self: self-start;
    gap: prem(8);

    h1 {
      font-weight: bold;
    }

    span {
      color: var(--ds-secondary-message-color);
      font-size: 0.9rem;
    }
  }
}

.card-book.layout-grid {
  height: fit-content;
  width: 180px;

  flex-direction: column;
  align-items: center;
}

.card-book.layout-list {
  height: 250px;
  width: 100%;

  transform-origin: center left;
}
</style>
