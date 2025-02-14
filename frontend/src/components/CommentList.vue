<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-comments">
    <div v-for="comment in allComments" :key="comment.id" class="comment">
      <p><strong>{{ comment.user.username }}</strong></p>
      <p>{{ comment.content }}</p>
      <small>{{ comment.created_at }} - لایک‌ها: {{ comment.like_count }}</small>
      <button @click="toggleMaktabLike(comment.id)">لایک</button>
      <maktab-comment-list v-if="comment.replies" :comments="comment.replies"></maktab-comment-list>
    </div>
    <form @submit.prevent="submitMaktabComment">
      <textarea v-model="newComment.content" placeholder="افزودن نظر"></textarea>
      <button type="submit">ارسال</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'MaktabCommentList',
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
    async submitMaktabComment() {
      // ارسال کامنت جدید و به‌روزرسانی لیست کامنت‌ها
      await this.addComment(this.newComment);
      this.newComment.content = '';
      this.fetchComments(this.postId);
    },
    toggleMaktabLike(commentId) {
      // تغییر وضعیت لایک کامنت
      this.likeComment(commentId);
    },
  },
  created() {
    // دریافت کامنت‌ها برای پست مشخص شده هنگام ساخت کامپوننت
    this.fetchComments(this.postId);
  },
};
</script>

<style scoped>
.maktab-comments {
  padding: 20px;
  /* استایل‌دهی به بخش کامنت‌ها */
}
.comment {
  background: #f9f9f9;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  /* استایل‌دهی به هر کامنت */
}
form {
  margin-top: 20px;
  /* استایل‌دهی به فرم ارسال کامنت جدید */
}
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  /* استایل‌دهی به فیلد متنی کامنت */
}
button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  margin-top: 10px;
  /* استایل‌دهی به دکمه‌ها */
}
button:hover {
  background-color: #00796b;
  /* استایل‌دهی دکمه در حالت هاور */
}
</style>
