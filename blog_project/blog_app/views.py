import requests
from django.shortcuts import render, redirect
from .models import BlogPost

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
AUTH_HEADER = {"Authorization": "Bearer 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"}

def classify_blog_content(content):
    data = {
        "inputs": content,
        "parameters": {
            "candidate_labels": ["technology", "sports", "entertainment", "politics", "health", "education", "science", "business", "travel", "fashion" ],
        }
    }
    
    response = requests.post(API_URL, headers=AUTH_HEADER, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            result = response.json()
            
            # Safely access the 'labels' and 'scores' keys
            if 'labels' in result and len(result['labels']) > 0:
                return result['labels'][0]  # Return the most probable category (first label)
        except (KeyError, IndexError):
            pass  # Handle any unexpected response format
    
    # Default to 'Uncategorized' if the API call fails or doesn't return expected data
    return 'Uncategorized'

def blog_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        # Classify blog content
        category = classify_blog_content(content)

        # Create blog post
        blog_post = BlogPost(title=title, content=content, category=category)
        blog_post.save()
        return redirect('blog_list')

    return render(request, 'blog/blog_create.html')

def blog_list(request):
    blogs = BlogPost.objects.all()
    categorized_blogs = {}
    for blog in blogs:
        if blog.category not in categorized_blogs:
            categorized_blogs[blog.category] = []
        categorized_blogs[blog.category].append(blog)
    
    return render(request, 'blog/blog_list.html', {'categorized_blogs': categorized_blogs})
