<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-post-details">
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <maktab-comment-list :postId="post.id"></maktab-comment-list>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import MaktabCommentList from '@/components/CommentList.vue';

export default {
  name: 'MaktabPostDetails',
  components: {
    MaktabCommentList,
  },
  computed: {
    ...mapState(['post']),
  },
};
</script>

<style scoped>
.maktab-post-details {
  padding: 20px;
  /* استایل‌دهی به جزئیات پست */
}
</style>
