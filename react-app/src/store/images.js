//constants
const LOAD_IMAGE = 'images/LOAD_IMAGE';
const LOAD_IMAGES = 'images/LOAD_IMAGES';
const ADD_IMAGE = 'images/ADD_IMAGE';
const REMOVE_IMAGE = 'images/REMOVE_IMAGE';
const EDIT_IMAGE = 'images/EDIT_IMAGE';

const LOAD_COMMENTS = 'images/LOAD_COMMENTS';
const ADD_COMMENT = 'images/ADD_COMMENT';
const DELETE_COMMENT = 'images/DELETE_COMMENT';
const EDIT_COMMENT = 'images/EDIT_COMMENT';

const ADD_TAG = 'images/ADD_TAG';
const DELETE_TAG = 'images/DELETE_TAG';

// Images

const loadImage = (image) => ({
    type: LOAD_IMAGE,
    payload: image
})

const loadImages = (images) => ({
    type: LOAD_IMAGES,
    payload: images
})

const addImagePost = (image) => ({
    type: ADD_IMAGE,
    payload: image
});

const removeImage = (imageId) => ({
    type: REMOVE_IMAGE,
    payload: imageId
});

const changePost = (editedPost) => ({
    type: EDIT_IMAGE,
    payload: editedPost
});

// Comments

const loadComments = (comments) => ({
    type: LOAD_COMMENTS,
    payload: comments
});

const addComment = (newComment) => ({
    type: ADD_COMMENT,
    payload: newComment
});

const deleteComment = (deletedComment) => ({
    type: DELETE_COMMENT,
    payload: deletedComment
});

const editComment = (editedComment) => ({
    type: EDIT_COMMENT,
    payload: editedComment
});

//Tags

const createTag = (postIdAndTag) => ({
    type: ADD_TAG,
    payload: postIdAndTag
});

const deleteTag = (tagToDelete) => ({
    type: DELETE_TAG,
    payload: tagToDelete
});

export const getImages = (page = 1) => async (dispatch) => {

    console.log(`getting all images`)

    const data = await fetch(`/api/images/page/${page}/`);

    if(data.ok) {
        const response = await data.json();
        dispatch(loadImages(response))
    }
}

export const getImage = (id) => async (dispatch) => {

    console.log(`getting image ${id}`)

    const data = await fetch(`/api/images/${id}/`);

    if(data.ok) {
        const response = await data.json();
        dispatch(loadImage(response));
        return response;
    }
}

export const addImage = post => async (dispatch) => {
    const data = await fetch('/api/images/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(post)
    })

    if(data.ok) {
        const response = await data.json();

        dispatch(addImagePost(response));
        return response;
    }

    return 'COULDN\'T ADD POST';
}

export const deleteImage = id => async (dispatch) => {
    const data = await fetch(`/api/images/${id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    if(data.ok) {
        const deletedPostId = await data.json();
        dispatch(removeImage(deletedPostId));
    }
}

export const editImage = post => async (dispatch) => {
    const data = await fetch(`/api/images/${post.id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(post)
    });

    if(data.ok) {
        const response = await data.json();
        dispatch(changePost(response))
    }
}

export const addCommentToPost = (comment) => async (dispatch) => {
    const data = await fetch(`/api/comments/${comment.postId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    });

    if(data.ok) {
        const response = await data.json();
        dispatch(addComment(response));
    }
}

export const editPostComment = (comment) => async (dispatch) => {
    const data = await fetch(`/api/comments/${comment.id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    });

    if(data.ok) {
        const response = await data.json();
        dispatch(editComment(response));
    }
}

export const deletePostComment = (comment) => async (dispatch) => {
    const data = await fetch(`/api/comments/${comment.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if(data.ok) {
        // const response = await data.json();
        dispatch(deleteComment(comment));
    }
}


// IMAGE TAGS

export const addTagToPost = (tag, postId) => async (dispatch) => {
    const data = await fetch(`/api/tags/${+postId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({tag})
    });

    if(data.ok) {
        const response = await data.json();
        response.postId = postId
        dispatch(createTag(response))
    }
}

export const deleteTagFromPost = (tag, postId) => async (dispatch) => {
    const data = await fetch(`/api/tags/${postId}/${tag.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if(data.ok) {
        const response = await data.json();
        dispatch(deleteTag({ response, postId }));
    }
}

// SEARCH

export const searchForPosts = (query) => async (dispatch) => {
    const data = await fetch(`/api/tags/search/${query}/`);

    if(data.ok) {
        const response = await data.json();
        console.log('searchForPosts ~ response', response);

        dispatch(loadImages(response));
    }
}

export default function imagesReducer(state = {}, action) {
    switch (action.type) {
        case LOAD_IMAGE: {
            const newState = { ...state };

            newState[action.payload.id] = action.payload;
            // console.log('imagesReducer ~ action.payload', action.payload);

            const newComments = {};
            for(let comment of action.payload.comments) {
                newComments[comment.id] = comment
            }
            newState[action.payload.id].comments = newComments;

            const tags = {};
            for(let tag of action.payload.tags) {
                tags[tag.id] = tag;
            }
            newState[action.payload.id].tags = tags;


            return newState;
        }
        case LOAD_IMAGES: {
            const newState = {};

            for(let i = 0; i < action.payload.length; i++) {
                newState[action.payload[i].id] = action.payload[i];
            }

            return newState;
        }
        case ADD_IMAGE: {
            const newState = { ...state };
            newState[action.payload.id] = action.payload;

            return newState;
        }
        case REMOVE_IMAGE: {
            const newState = { ...state };

            delete newState[action.payload];

            return newState;
        }
        case EDIT_IMAGE: {
            const newState = { ...state };
            newState[action.payload.id] = action.payload;

            return newState;
        }
        case ADD_COMMENT: {
            const newState = {
                ...state,
                [action.payload.postId]: {
                    ...state[action.payload.postId],
                    comments: {
                        ...state[action.payload.postId].comments,
                        [action.payload.id]: action.payload
                    }
                }
            };

            return newState;
        }
        case EDIT_COMMENT: {
            const newState = {
                ...state,
                [action.payload.postId]: {
                    ...state[action.payload.postId],
                    comments: {
                        ...state[action.payload.postId].comments,
                    }
                }
            };

            newState[action.payload.postId].comments[action.payload.id] = action.payload

            return newState;
        }
        case DELETE_COMMENT: {
            const newState = {
                ...state,
                [action.payload.postId]: {
                    ...state[action.payload.postId],
                    comments: {
                        ...state[action.payload.postId].comments,
                    }
                }
            };

            delete newState[action.payload.postId].comments[action.payload.id]

            return newState;
        }
        case ADD_TAG: {
            const newState = {
                ...state,
                [action.payload.postId]: {
                    ...state[action.payload.postId],
                    tags: {
                        ...state[action.payload.postId].tags,
                        [action.payload.id]: action.payload
                    }
                }
            }

            return newState;
        }
        case DELETE_TAG: {
            const newTags = { ...state[action.payload.postId].tags };
            delete newTags[action.payload.response.id]

            const newState = {
                ...state,
                [action.payload.postId]: {
                    ...state[action.payload.postId],
                    tags: newTags
                }
            }

            return newState;
        }
      default:
            return state;
    }
}
