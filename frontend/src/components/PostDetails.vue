<!-- PostDetails.vue -->
<template>
    <div class="post-details">
      <h2>{{ post.title }}</h2>
      <p>{{ post.content }}</p>
      <comment-list :postId="post.id"></comment-list>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  import CommentList from '@/components/CommentList.vue';
  
  export default {
    name: 'PostDetails',
    components: {
      CommentList,
    },
    computed: {
      ...mapState(['post']),
    },
  };
  </script>
  
  <style scoped>
  .post-details {
    padding: 20px;
  }
  </style>
  