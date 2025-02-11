<!-- CommentList.vue -->
<template>
    <div class="comments">
      <div v-for="comment in allComments" :key="comment.id" class="comment">
        <p><strong>{{ comment.user.username }}</strong></p>
        <p>{{ comment.content }}</p>
        <small>{{ comment.created_at }} - Likes: {{ comment.like_count }}</small>
        <button @click="toggleLike(comment.id)">Like</button>
        <comment-list v-if="comment.replies" :comments="comment.replies"></comment-list>
      </div>
      <form @submit.prevent="submitComment">
        <textarea v-model="newComment.content" placeholder="افزودن نظر"></textarea>
        <button type="submit">ارسال</button>
      </form>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex';
  
  export default {
    name: 'CommentList',
    props: ['postId', 'comments'],
    data() {
      return {
        newComment: {
          content: '',
          post: this.postId,
        },
      };
    },
    computed: {
      ...mapGetters(['allComments']),
    },
    methods: {
      ...mapActions(['fetchComments', 'addComment', 'likeComment']),
      async submitComment() {
        await this.addComment(this.newComment);
        this.newComment.content = '';
        this.fetchComments(this.postId);
      },
      toggleLike(commentId) {
        this.likeComment(commentId);
      },
    },
    created() {
      this.fetchComments(this.postId);
    },
  };
  </script>
  
  <style scoped>
  .comments {
    padding: 20px;
  }
  .comment {
    background: #f9f9f9;
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
  }
  form {
    margin-top: 20px;
  }
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  button {
    background-color: #004d40;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    margin-top: 10px;
  }
  button:hover {
    background-color: #00796b;
  }
  </style>
  