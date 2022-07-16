from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from app.forms import CreatePostForm, EditPostForm, CreateTagForm
from app.models import db, Post, Tag
from app.api.utils import validation_errors_to_error_messages
from sqlalchemy import desc, asc
from PIL import Image
import requests
from io import BytesIO
from numpy import asarray
import math
from app.api.s3_upload import delete_image_from_bucket

images_routes = Blueprint('images', __name__)

# GET ALL IMAGES
@images_routes.route('/page/<int:page>/')
def get_images(page):
    posts = Post.query.order_by(desc(Post.createdAt)).all()
    posts = [post.to_dict_lite() for post in posts]

    # posts = Post.query.order_by(desc(Post.createdAt)).paginate(page=page, per_page=20, error_out=False)
    # posts = [post.to_dict_lite() for post in posts.items]

    return jsonify(posts)


# GET SINGLE IMAGE
@images_routes.route('/<int:postId>/')
def get_single_image(postId):
    post = Post.query.get(postId)

    response = requests.get(post.postImageUrl)
    img = Image.open(BytesIO(response.content))
    data = asarray(img)

    red_count = 0
    green_count = 0
    blue_count = 0

    yellow_count = 0
    cyan_count = 0
    magenta_count = 0

    violet_count = 0
    raspberry_count = 0
    ocean_count = 0
    turquoise_count = 0
    spring_green_count = 0
    orange_count = 0

    white_count = 0
    black_count = 0
    gray_count = 0

    total_count = 0

    red_pixels = []

    #to know if a pixel is red, green, or blue, we take the average of the 3 values (rgb) and if the color we are looking for
    #is above that average, then it is close to that color

    for row in data:
        for pixel in row:
            red = int(pixel[0])
            green = int(pixel[1])
            blue = int(pixel[2])

            average = int((red + green + blue) / 3)

            if (red > 240 and green > 240 and blue > 240):
                white_count += 1
                total_count += 1
                continue
            if red < 50 and green < 50 and blue < 50:
                black_count += 1
                total_count += 1
                continue
            if max(pixel) - min(pixel) < 20:
                gray_count += 1
                total_count += 1
                continue

            if red > average:
                if blue > average:
                    if 65 < blue < 190:
                        raspberry_count += 1
                        total_count += 1
                        continue
                    elif 65 < red < 190:
                        violet_count += 1
                        total_count += 1
                        continue
                    elif (190 < red < 255) and (190 < blue  < 255):
                        magenta_count += 1
                        total_count += 1
                        continue
                if green > average:
                    if 65 < green < 190:
                        orange_count += 1
                        total_count += 1
                        continue
                    elif 65 < red < 190:
                        spring_green_count += 1
                        total_count += 1
                        continue
                    elif (190 < red < 255) and (190 < green < 255):
                        yellow_count += 1
                        total_count += 1
                        continue
                else:
                    red_count += 1
                    total_count += 1
                    continue
            if green > average:
                if blue > average:
                    if 65 < green < 190:
                        ocean_count += 1
                        total_count += 1
                        continue
                    elif 65 < blue < 190:
                        turquoise_count += 1
                        total_count += 1
                        continue
                    elif (190 < blue < 255) and (190 < green < 255):
                        cyan_count += 1
                        total_count += 1
                        continue
                else:
                    green_count += 1
                    total_count += 1
                    continue
            if blue_count > average:
                blue_count += 1
                total_count += 1
                continue


    print('\nred:', int(red_count / (img.width * img.height) * 100), '% - ', red_count)
    print('\ngreen:', int(green_count / (img.width * img.height) * 100), '% - ', green_count)
    print('\nblue:', int(blue_count / (img.width * img.height) * 100), '% - ', blue_count)

    print('\nyellow:', int(yellow_count / (img.width * img.height) * 100), '% - ', yellow_count)
    print('\ncyan:', int(cyan_count / (img.width * img.height) * 100), '% - ', cyan_count)
    print('\nmagenta:', int(magenta_count / (img.width * img.height) * 100), '% - ', magenta_count)

    print('\nviolet:', int(violet_count / (img.width * img.height) * 100), '% - ', violet_count)
    print('\nraspberry:', int(raspberry_count / (img.width * img.height) * 100), '% - ', raspberry_count)
    print('\nocean:', int(ocean_count / (img.width * img.height) * 100), '% - ', ocean_count)
    print('\nturquoise:', int(turquoise_count / (img.width * img.height) * 100), '% - ', turquoise_count)
    print('\nspring_green:', int(spring_green_count / (img.width * img.height) * 100), '% - ', spring_green_count)
    print('\norange:', int(orange_count / (img.width * img.height) * 100), '% - ', orange_count)

    print('\nwhite:', int(white_count / (img.width * img.height) * 100), '% - ', white_count)
    print('\nblack:', int(black_count / (img.width * img.height) * 100), '% - ', black_count)
    print('\ngray:', int(gray_count / (img.width * img.height) * 100), '% - ', gray_count)

    print('\n\nTotal pixels matched:', int(total_count / (img.height * img.width) * 100), '%\n\n')
    print('\n\nTotal pixels in image:', total_count, '/', img.height * img.width, '\n\n')

    if post:
        post_to_dict = post.to_dict()
        # post_to_dict['pixelArray'] = data
        return jsonify(post_to_dict)
    else:
        return jsonify('Not found'), 401


# UPLOAD IMAGE
@images_routes.route('/', methods=["POST"])
def create_image():
    form = CreatePostForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = {
            "userId": session['_user_id'],
            "postImageUrl": form.data["postImageUrl"],
            "title": form.data["title"]
        }

        post = Post(**data)
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict())

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@images_routes.route('/<int:postId>/', methods=['DELETE'])
def delete_image(postId):
    image = Post.query.get(postId)
    sessionUserId = session['_user_id']

    if image.to_dict()['userId'] == int(sessionUserId):
        delete_image_from_bucket(image.to_dict_lite())
        db.session.delete(image)
        db.session.commit()
        return jsonify(postId)
    else:
        return jsonify('Invalid Request'), 401


@images_routes.route('/<int:postId>/', methods=['PUT'])
def edit_image(postId):
    post = Post.query.get(postId)
    form = EditPostForm()
    userId = session['_user_id']

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if int(userId) != int(post.userId):
            return jsonify('Invalid Request'), 401
        else:
            post.title = form['title'].data
            db.session.commit()
            return jsonify(post.to_dict())

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
