import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useHistory } from 'react-router-dom';

import * as imageActions from '../../store/images';
import LoadingAnimation from '../LoadingAnimation';
// import PostModal from '../PostModal/PostModal';
import './FeedPage.css';

export default function FeedPage() {
    const dispatch = useDispatch();
    let images = useSelector(state => Object.values(state.images).reverse().filter(image => 'id' in image));
    // console.log('FeedPage ~ images', images);

    const [isLoaded, setIsLoaded] = useState(false);
    // const [nextImages, setNextImages] = useState(2);

    useEffect(() => {
        (async () => {
            await dispatch(imageActions.getImages());
            setIsLoaded(true);
        })()
    }, []);

    // useEffect(() => {
    //     const scrolling_function = async () => {
    //         if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight + 100) {
    //             window.removeEventListener('scroll', scrolling_function);
    //             await dispatch(imageActions.getImages(nextImages));
    //             setNextImages(prev => prev + 1);
    //         }
    //     }

    //     window.addEventListener('scroll', scrolling_function);

    //     return () => {
    //         window.removeEventListener('scroll', scrolling_function);
    //     }
    // }, [nextImages]);

    return !isLoaded ?
        <LoadingAnimation />

        :

        <>
            {images.length > 0 ?
                <div id='feed-images'>
                    {images?.map(image => {
                        return image.id && (
                            <div className='single-feed-post' key={image?.id}>
                                <Link to={`/pictures/${image?.id}`}>
                                    <img src={image?.postImageUrl} alt='something goes here' className='feed-post-image'/>
                                </Link>
                            </div>
                        )
                    })}
                </div>

            :

                <h1>No posts found</h1>
            }
        </>
}
