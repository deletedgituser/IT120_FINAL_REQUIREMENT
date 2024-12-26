from django.contrib import admin
from .models import Message
from server_app.middlewares.encryption_middleware import EncryptionMiddleware

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'encrypted_content', 'decrypted_content', 'timestamp')  # Display these fields in the admin list view
    search_fields = ('sender__username', 'recipient__username', 'encrypted_content')  # Enable searching
    list_filter = ('timestamp', 'sender', 'recipient')  # Add filters for better usability
    ordering = ('-timestamp',)  # Order messages by most recent
    readonly_fields = ('timestamp',)  # Make timestamp read-only

    def decrypted_content(self, obj):
        mid_instance = EncryptionMiddleware(None)
        try:
            return mid_instance.decrypt_text(obj.encrypted_content)  # Call your decryption function
        except Exception as e:
            return f"Error: {str(e)}"  # Handle any decryption errors gracefully

    decrypted_content.short_description = "Decrypted Content"